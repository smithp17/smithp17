<div align="center">

<img src="./assets/hero.svg" width="100%" alt="SMIT PATNE - Full-Stack Engineer x GenAI Developer"/>

**I build AI products end to end: the model, the API, the UI, and the Docker setup that ships it.**

Mumbai, India &nbsp;·&nbsp; open to GenAI / Full-Stack / Applied ML roles

</div>

<br/>

<img src="./assets/player-card.svg" width="100%" alt="Player card: GenAI 92, Backend 90, Frontend 82, ML 80, Data 76, Debugging at 2am: over 9000"/>

<br/>

## Levels cleared

> Click any level to open it.

<details>
<summary><b>1-1 &nbsp; DataForge</b> &nbsp;·&nbsp; <i>don't search for data, generate it</i> &nbsp;<code>NOW PLAYING</code></summary>
<br/>

My startup. You describe a dataset in plain English (or list some column names, describe a scenario, or upload a sample) and it generates one.

The hard part isn't generating rows. It's generating rows that agree with each other: foreign keys that resolve, dates in the right order, distributions that look like a real system made them.

`React` `FastAPI` `PostgreSQL` `Ollama (mistral:7b)` `Docker`
</details>

<details>
<summary><b>1-2 &nbsp; Pharma Compliance LMS</b> &nbsp;·&nbsp; <i>where the auditor is the final boss</i> &nbsp;<code>PILOT LIVE</code></summary>
<br/>

A multi-tenant learning and compliance platform for pharma companies.

- Tenant isolation in Postgres with row-level security, not in app code
- Audit events are append-only, hash-chained, and stored on WORM storage
- Exam sessions are server-authoritative, so the browser is never trusted
- Hybrid BM25 + vector search, because pure vector search is bad at exact regulatory terms
- 120+ numbered architecture decisions and counting

`FastAPI` `PostgreSQL + pgvector` `SCORM` `xAPI` `React Native`
</details>

<details>
<summary><b>2-1 &nbsp; FraudShield AI</b> &nbsp;·&nbsp; <i>catching card fraud in real time</i></summary>
<br/>

A transaction stream goes through feature engineering, then an XGBoost model, then a decision service. Every block comes with SHAP values, so there's always a reason attached.

`Kafka` `Redis` `XGBoost` `SHAP` `MLflow` `Prometheus` `Grafana`
</details>

<details>
<summary><b>2-2 &nbsp; FinSight AI</b> &nbsp;·&nbsp; <i>ask questions about your portfolio</i></summary>
<br/>

Financial RAG over your documents plus live market data, split across five services.

`pgvector` `Jina embeddings` `Perplexity API` `Finnhub`
</details>

<details>
<summary><b>3-1 &nbsp; ShelfScanner AI</b> &nbsp;·&nbsp; <i>computer vision vs. the cereal aisle</i></summary>
<br/>

Counts every product on a retail shelf and identifies each one by SKU. Shelves are packed with hundreds of near-identical boxes, which is where standard detection falls apart, so I wrote strict labelling rules and tuned NMS for density.

`YOLO11` `CLIP`
</details>

<details>
<summary><b>3-2 &nbsp; PitchFieldAI</b> &nbsp;·&nbsp; <i>an LLM that actually watches cricket</i></summary>
<br/>

Player intelligence for cricket and football, built on an LLM fine-tuned with LoRA instead of a RAG chatbot wearing a jersey.

`LoRA` `PEFT` `Hugging Face`
</details>

<details>
<summary><b>4-1 &nbsp; ZK Private Voting</b> &nbsp;·&nbsp; <i>prove you voted without showing how</i></summary>
<br/>

Private voting built from scratch on zero-knowledge proofs. Anyone can verify the tally without seeing a single ballot.

`Solidity` `Go` `Node.js`
</details>

<br/>

## Bosses defeated

| Boss | What it did | How it went down |
|---|---|---|
| The Silent Exit | Frontend container died instantly. No error, no logs. | No TTY. One line in docker-compose. One lost evening. |
| The Blank Page | React rendered nothing at all | A browser wallet extension was locking down JS. Incognito gave it away. |
| The Year 2262 | Synthetic timestamps crashed the generator | pandas nanosecond timestamps stop at 2262-04-11. |
| The Phantom Topic | Kafka "working", nothing arriving | Producer and consumer were on different topics. Both very confident. |
| The Empty Dashboard | Grafana loaded perfectly and showed nothing | Datasource UID mismatch |
| The VRAM Golem | Video model out of memory on a free GPU | CPU offload + VAE slicing. Got a full music video out of Kaggle's free tier. |

<br/>

## Two truths and a lie

1. I write Hinglish science songs for an Instagram page.
2. I fine-tuned an LLM so it could argue about cricket and football.
3. I benchmarked Claude, GPT and Gemini on object detection, and Claude won.

<details>
<summary><b>Reveal</b></summary>
<br/>

Number 3 is the lie. Gemini won. The other two are completely true.
</details>

<br/>

## Inventory

```
languages   python · typescript · javascript · sql · java
ai / ml     langchain · openai · hugging face · ollama · lora · xgboost · mlflow · yolo · clip
web         react · react native · tailwind · fastapi · node · spring boot
data        postgres + pgvector · mongodb · redis · kafka · airflow · snowflake · bigquery
ops         docker · kubernetes · aws · gcp · prometheus · grafana
```

<br/>

<img src="./assets/continue.svg" width="100%" alt="Continue? Player 2 has entered the game"/>

<div align="center">

[![Email](https://img.shields.io/badge/INSERT_COIN-email_me-FF6B6B?style=for-the-badge)](mailto:smithp17999@gmail.com?subject=Player%202%20has%20entered%20the%20game)
[![LinkedIn](https://img.shields.io/badge/CO--OP-LinkedIn-0077B5?style=for-the-badge)](https://www.linkedin.com/in/smit-patne/)
[![Portfolio](https://img.shields.io/badge/WORLD_MAP-portfolio-4ECDC4?style=for-the-badge)](https://smitpatneportfolio.netlify.app/)

<sub>Off the clock: cricket, football, and defending Vinícius Júnior in group chats.</sub>

</div>
