from elasticsearch import Elasticsearch
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import logging
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)

es = Elasticsearch(hosts=["http://elasticsearch:9200"])
INDEX_NAME = "documents"

initial_texts = [
    "India, officially the Republic of India, is a country in South Asia. It is the seventh-largest country by area; the most populous country from June 2023 onwards; and since its independence in 1947, the world's most populous democracy. Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west; China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is near Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar, and Indonesia.",
    "Modern humans arrived on the Indian subcontinent from Africa no later than 55,000 years ago. Their long occupation, predominantly in isolation as hunter-gatherers, has made the region highly diverse, second only to Africa in human genetic diversity. Settled life emerged on the subcontinent in the western margins of the Indus river basin 9,000 years ago, evolving gradually into the Indus Valley Civilisation of the third millennium BCE. By 1200 BCE, an archaic form of Sanskrit, an Indo-European language, had diffused into India from the northwest. Its hymns recorded the dawning of Hinduism in India. India's pre-existing Dravidian languages were supplanted in the northern regions. By 400 BCE, caste had emerged within Hinduism, and Buddhism and Jainism had arisen, proclaiming social orders unlinked to heredity. Early political consolidations gave rise to the loose-knit Maurya and Gupta Empires. Widespread creativity suffused this era, but the status of women declined, and untouchability became an organized belief. In South India, the Middle kingdoms exported Dravidian language scripts and religious cultures to the kingdoms of Southeast Asia.",
    "In the early mediaeval era, Christianity, Islam, Judaism, and Zoroastrianism became established on India's southern and western coasts. Muslim armies from Central Asia intermittently overran India's northern plains. The resulting Delhi Sultanate drew northern India into the cosmopolitan networks of mediaeval Islam. In south India, the Vijayanagara Empire created a long-lasting composite Hindu culture. In the Punjab, Sikhism emerged, rejecting institutionalised religion. The Mughal Empire, in 1526, ushered in two centuries of relative peace, leaving a legacy of luminous architecture. Gradually expanding rule of the British East India Company turned India into a colonial economy but consolidated its sovereignty. British Crown rule began in 1858. The rights promised to Indians were granted slowly, but technological changes were introduced, and modern ideas of education and public life took root. A pioneering and influential nationalist movement, noted for nonviolent resistance, became the major factor in ending British rule. In 1947, the British Indian Empire was partitioned into two independent dominions, a Hindu-majority dominion of India and a Muslim-majority dominion of Pakistan. A large-scale loss of life and an unprecedented migration accompanied the partition.",
    "India has been a federal republic since 1950, governed through a democratic parliamentary system. It is a pluralistic, multilingual and multi-ethnic society. India's population grew from 361 million in 1951 to over 1.4 billion in 2023. During this time, its nominal per capita income increased from US$64 annually to US$2,601, and its literacy rate from 16.6% to 74%. A comparatively destitute country in 1951, India has become a fast-growing major economy and hub for information technology services; it has an expanding middle class. Indian movies and music increasingly influence global culture. India has reduced its poverty rate, though at the cost of increasing economic inequality. It is a nuclear-weapon state that ranks high in military expenditure. It has disputes over Kashmir with its neighbours, Pakistan and China, unresolved since the mid-20th century. Among the socio-economic challenges India faces are gender inequality, child malnutrition, and rising levels of air pollution. India's land is megadiverse with four biodiversity hotspots. India's wildlife, which has traditionally been viewed with tolerance in its culture, is supported in protected habitats."
]

initial_docs = [{"id": i+1, "text": text} for i, text in enumerate(initial_texts)]

# since elasticsearch takes some time to start up, we need to wait for it
def start_elasticsearch():
    for i in range(30):
        try:
            if es.ping():
                logger.info("Elasticsearch is up and reachable!")
                return
        except Exception:
            logger.warning(f"[{i+1}/30] Waiting for Elasticsearch to be ready...")
        time.sleep(2)
    raise Exception("Elasticsearch is not reachable after waiting.")

def insert_initial_docs():
    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(index=INDEX_NAME, ignore=400)
        logger.info(f"Created index: {INDEX_NAME}")

    for doc in initial_docs:
        try:
            if not es.exists(index=INDEX_NAME, id=doc["id"]):
                es.index(index=INDEX_NAME, id=doc["id"], body=doc)
                logger.info(f"Inserted initial doc ID {doc['id']}")
            else:
                logger.info(f"Doc ID {doc['id']} already exists, skipping insert.")
        except Exception as e:
            logger.error(f"Error inserting doc ID {doc['id']}: {e}")

start_elasticsearch()
insert_initial_docs()

@app.options("/insert")
def preflight_insert():
    return Response(status_code=200)

@app.options("/search")
def preflight_search():
    return Response(status_code=200)

@app.post("/insert")
async def insert_doc(doc: dict):
    try:
        res = es.index(index=INDEX_NAME, body=doc)
        logger.info(f"Inserted new document: {doc}")
        return {"result": "success", "id": res["_id"]}
    except Exception as e:
        logger.error(f"Insertion failed: {e}")
        return {"error": str(e)}

@app.post("/search")
async def search_doc(query: dict):
    try:
        es_query = {
            "query": {
                "match": {
                    "text": query["query"]
                }
            },
            "size": 1
        }
        res = es.search(index=INDEX_NAME, body=es_query)
        hits = res["hits"]["hits"]
        if hits:
            return {"text": hits[0]["_source"]["text"]}
        else:
            return {"text": "No match found in documents."}
    except Exception as e:
        logger.error(f"Search failed: {e}")
        return {"error": str(e)}
