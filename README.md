<!--
  👋 Hi, you're reading the source. Respect.
  SETUP: find & replace  YOUR_GH_USERNAME  with your GitHub username (5 spots).
-->

<div align="center">

<img src="./assets/hero.svg" width="100%" alt="SMIT PATNE — Full-Stack Engineer × GenAI Developer — Press Start"/>

<br/>

**You found a playable profile.** One credit inserted. Almost everything below opens when you click it. ▸

<sub>👀 HIGH SCORE:</sub> <img src="https://komarev.com/ghpvc/?username=YOUR_GH_USERNAME&label=PLAYERS%20SO%20FAR&color=FF6B6B&style=flat-square" alt="visitor count"/>

</div>

---

## 🕹️ SELECT YOUR PLAYER

<table>
<tr>
<td width="50%" valign="top">

<details>
<summary><b>🧑‍💼 &nbsp;I'm hiring</b> &nbsp;<sub>· speedrun mode (30 sec)</sub></summary>
<br/>

> **TL;DR:** I build AI products end-to-end: the RAG pipeline, the API behind it, the React UI in front of it, and the Docker setup that ships it.

- 🎯 **Looking for:** GenAI Engineer · Full-Stack · Applied ML roles
- 📍 **Based in:** Mumbai, India · open to remote & relocation
- 🧾 **Proof, not adjectives:**
  - Shipped a multi-tenant **pharma compliance LMS**, now running with pilot customers (RLS, hash-chained audit log, hybrid RAG)
  - Built **FraudShield AI**, a real-time fraud platform on Kafka + XGBoost + SHAP + MLflow
  - Founding **DataForge**, an AI synthetic-dataset generator
- ⏱️ **Fastest route:** [📧 email me](mailto:smithp17999@gmail.com?subject=Player%202%20has%20entered%20the%20game) or [💼 LinkedIn](https://www.linkedin.com/in/smit-patne/)

</details>

<details>
<summary><b>🚀 &nbsp;I'm building something</b> &nbsp;<sub>· co-op mode</sub></summary>
<br/>

I like zero-to-one. My default loop: **idea → schema → API → UI → Docker → real users**, with an architecture decision log the whole way (one of my projects is past 120 numbered decisions).

If you have an AI-first product that needs someone to own it end to end, from model choice to the deploy, we should talk.

→ [Pitch me](mailto:smithp17999@gmail.com?subject=Co-op%20mode%3A%20let%27s%20build)

</details>

</td>
<td width="50%" valign="top">

<details>
<summary><b>👩‍💻 &nbsp;I'm a fellow dev</b> &nbsp;<sub>· versus mode</sub></summary>
<br/>

Skip to the **[👹 Boss Rush](#-boss-rush--bugs-ive-defeated)**: real bugs, real fixes, mild trauma.

Things I'll happily nerd out about:
- Hybrid BM25 + dense retrieval vs. pure vector search
- Why your Kafka consumer is "working" but nothing arrives
- Row-level security as a multi-tenancy strategy
- Getting video diffusion models to run on free GPUs

</details>

<details>
<summary><b>🎲 &nbsp;I'm just wandering</b> &nbsp;<sub>· free play</sub></summary>
<br/>

Welcome, traveller. Try the **[🎲 Two Truths & a Lie](#-two-truths--a-lie)**, check out my **[🧭 Side Quests](#-side-quests)**, and look for the hidden level. There is one. 🔒

</details>

</td>
</tr>
</table>

---

## 🧙 PLAYER CARD

<div align="center">
<img src="./assets/player-card.svg" width="100%" alt="Character sheet: Full-Stack Mage. GenAI/RAG 92, Backend 90, Frontend 82, ML & MLOps 80, Data & Streaming 76, Debugging at 2am: over 9000."/>
</div>

---

## 🗺️ WORLD MAP

> Each level is a real project. Click a level to see the boss I had to beat.

<details>
<summary><b>🌋 WORLD 1-1 · DataForge</b> &nbsp;—&nbsp; <i>"Don't search for data. Generate it."</i> &nbsp;<code>⭐⭐⭐⭐⭐</code> &nbsp;<code>🟢 NOW PLAYING</code></summary>
<br/>

**The quest:** an AI-powered generator for synthetic ML datasets. Describe what you need in plain English, list some column names, describe a scenario, or upload a sample, and get back data that is **statistically realistic and relationally consistent**.

**Boss:** keeping LLM output consistent across related tables, with foreign keys that actually match and distributions that look real, while running locally on a 7B model.

**Loot:** `React` `FastAPI` `PostgreSQL` `Ollama · mistral:7b` `Docker` · deployed on a VPS · dark industrial forge UI 🔥

</details>

<details>
<summary><b>🏥 WORLD 1-2 · Pharma Compliance LMS</b> &nbsp;—&nbsp; <i>enterprise learning where the auditors are the final boss</i> &nbsp;<code>⭐⭐⭐⭐⭐</code> &nbsp;<code>🟢 PILOT LIVE</code></summary>
<br/>

**The quest:** a multi-tenant learning and compliance platform for pharma companies, where every action has to stand up to a regulatory audit.

**Boss:** proving nobody tampered with the training records. **Win condition:** append-only, **hash-chained audit events on WORM storage**, plus server-authoritative exam sessions so nobody can game the test from the browser.

**Loot:** `FastAPI modular monolith` `PostgreSQL + pgvector + RLS` `Hybrid BM25 + dense RAG` `SCORM 1.2/2004` `xAPI` `React Native` · a living `DECISIONS.md` with 120+ entries

</details>

<details>
<summary><b>🛡️ WORLD 2-1 · FraudShield AI</b> &nbsp;—&nbsp; <i>catching fraud in real time</i> &nbsp;<code>⭐⭐⭐⭐</code></summary>
<br/>

**The quest:** real-time credit-card fraud detection built as microservices: transaction simulator → feature engineering → ML inference → decision service, plus a training pipeline and an API gateway.

**Boss:** explainability. A blocked transaction needs a *reason*, so every prediction ships with **SHAP** values.

**Loot:** `Kafka` `Redis` `XGBoost` `SHAP` `MLflow` `PostgreSQL` `Prometheus` `Grafana` `Docker`

</details>

<details>
<summary><b>📈 WORLD 2-2 · FinSight AI</b> &nbsp;—&nbsp; <i>ask your portfolio questions</i> &nbsp;<code>⭐⭐⭐⭐</code></summary>
<br/>

**The quest:** a financial RAG system built from five microservices (gateway, auth, stock, RAG, documents) that answers questions using your documents *and* live market data.

**Loot:** `pgvector` `Jina AI embeddings` `Perplexity API` `Finnhub`

</details>

<details>
<summary><b>🛒 WORLD 3-1 · ShelfScanner AI</b> &nbsp;—&nbsp; <i>computer vision vs. the cereal aisle</i> &nbsp;<code>⭐⭐⭐⭐</code></summary>
<br/>

**The quest:** detect and count every product on a retail shelf, then identify each one at the SKU level.

**Boss:** dense shelves. Hundreds of near-identical boxes packed tight is exactly where NMS breaks down. I wrote strict labelling rules (one box per physical facing), tuned NMS for density, and added a **CLIP gallery** for SKU matching. I also benchmarked Gemini, GPT and Claude on grounded object detection.

**Loot:** `YOLO 11` `CLIP` `Hybrid detector + VLM` · a full experiment report

</details>

<details>
<summary><b>🏏 WORLD 3-2 · PitchFieldAI</b> &nbsp;—&nbsp; <i>an LLM that actually knows the game</i> &nbsp;<code>⭐⭐⭐⭐</code></summary>
<br/>

**The quest:** player intelligence for cricket and football, built on a **self-improving fine-tuned LLM (LoRA / PEFT)** rather than a RAG chatbot wearing a jersey.

**Loot:** `LoRA` `PEFT` `Hugging Face`

</details>

<details>
<summary><b>🗳️ WORLD 4-1 · ZK Private Voting</b> &nbsp;—&nbsp; <i>prove you voted without revealing how</i> &nbsp;<code>⭐⭐⭐⭐⭐</code></summary>
<br/>

**The quest:** a private voting system built from scratch on **ZK-SNARKs**, where you can verify the tally without seeing a single ballot.

**Loot:** `Solidity` `Go` `Node.js` `Zero-knowledge proofs`

</details>

<details>
<summary><b>🎁 BONUS STAGES</b> &nbsp;—&nbsp; <i>smaller worlds, still fun</i></summary>
<br/>

- **Botfolio**: a RAG chatbot that answers questions about my resume (migrated from Firebase to pgvector + HF embeddings)
- **EventHub**: an Eventbrite-style platform with real-time Socket.io messaging

</details>

---

## 👹 BOSS RUSH · bugs I've defeated

> Anyone can list a tech stack. Here are the monsters that tech stack threw at me.

| | Boss | Special attack | How it went down |
|:-:|---|---|---|
| 👻 | **The Silent Exit** | Frontend container dies instantly. No error. No logs. Nothing. | Docker TTY config. The container had no terminal to hold it open. |
| 📜 | **The Empty Scroll** | Files get written… with zero bytes inside | Bypassed the broken write path with PowerShell `Set-Content` |
| 🦊 | **The SES Lockdown** | React refuses to render at all | A *browser wallet extension* was freezing JS intrinsics. Incognito exposed it. |
| ⏳ | **The Nanosecond Overflow** | Synthetic timestamps crash the generator | pandas `ns` timestamps stop at **year 2262**. Future dates need different units. |
| 📡 | **The Topic Phantom** | Kafka "works", but events vanish | Producer and consumer were on different topics. Both were very confident. |
| 📊 | **The Ghost Datasource** | Grafana dashboards: beautiful, and completely empty | Datasource UID mismatch between provisioning and dashboards |
| 🗿 | **The VRAM Golem** | Video diffusion model OOMs on a free GPU | CPU offload + VAE slicing. Generated a full music video on Kaggle's free tier. |

<div align="center"><sub>Bugs defeated: <b>all of the above</b> · Bugs currently respawning: <i>let's not talk about it</i></sub></div>

---

## 🎲 TWO TRUTHS & A LIE

> Guess which one is fake, then click to check.

1. 🎵 I write and publish **Hinglish science songs** on Instagram.
2. 🏏 I fine-tuned an LLM with LoRA so it could talk cricket *and* football.
3. 🤖 I benchmarked Claude, GPT and Gemini on locating products in shelf images, and **Claude came out on top**.

<details>
<summary><b>🔍 Reveal the lie</b></summary>
<br/>

**#3 is the lie.** 🎉 Gemini won on spatial localisation, and Claude came in behind on coordinate accuracy. The other two are completely true, and yes, the songs are as fun as they sound.

</details>

---

## 🧭 SIDE QUESTS

| | Quest | Status |
|:-:|---|:-:|
| 🎤 | Making science stick with **Hinglish educational songs** on Instagram | 🔁 ongoing |
| 🎬 | Generated a **World Cup 2026 music video** with LTX-Video on a free GPU | ✅ complete |
| ⚽ | Defending Vinícius Júnior in every group chat | 🔁 eternal |
| 🏏 | Watching cricket instead of fixing that one bug | 🔁 eternal |

---

## 🎒 INVENTORY

<details>
<summary><b>Open inventory</b> <sub>· 30+ items</sub></summary>
<br/>

**🧠 AI / ML**<br/>
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white)
![pgvector](https://img.shields.io/badge/pgvector-336791?style=flat-square&logo=postgresql&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-337AB7?style=flat-square)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLO-00FFFF?style=flat-square&logo=yolo&logoColor=black)

**⚡ Full-Stack**<br/>
![React](https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=flat-square&logo=typescript&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind-38B2AC?style=flat-square&logo=tailwindcss&logoColor=white)
![React Native](https://img.shields.io/badge/React_Native-20232A?style=flat-square&logo=react&logoColor=61DAFB)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=mysql&logoColor=white)

**🗄️ Data**<br/>
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=flat-square&logo=mongodb&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=flat-square&logo=snowflake&logoColor=white)
![BigQuery](https://img.shields.io/badge/BigQuery-669DF6?style=flat-square&logo=googlebigquery&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black)
![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white)
![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white)

**☁️ Ship it**<br/>
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?style=flat-square&logo=googlecloud&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat-square&logo=grafana&logoColor=white)

</details>

---

## 🐍 LIVE GAMEPLAY

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/YOUR_GH_USERNAME/YOUR_GH_USERNAME/output/snake-dark.svg"/>
  <img src="https://raw.githubusercontent.com/YOUR_GH_USERNAME/YOUR_GH_USERNAME/output/snake.svg" alt="A snake eating my GitHub contribution graph"/>
</picture>

<sub>A snake eating my contribution graph. Please keep feeding it.</sub>

</div>

---

<details>
<summary><sub>🔒 ???</sub></summary>
<br/>

<details>
<summary><sub>🔒 are you sure? it's just a locked door.</sub></summary>
<br/>

<details>
<summary><sub>🔓 ok fine.</sub></summary>
<br/>

### 🏆 SECRET LEVEL UNLOCKED

You're the kind of person who opens every door. I like that.

Put the words **"nanosecond overflow"** anywhere in your email and I'll know you made it here. **The first coffee is on me.** ☕

<sub>Achievement unlocked: <b>Completionist</b></sub>

</details>
</details>
</details>

---

<div align="center">

<img src="./assets/continue.svg" width="100%" alt="Continue? Player 2 has entered the game. Insert coin below."/>

<br/>

[![Email](https://img.shields.io/badge/🪙_INSERT_COIN-Email_me-FF6B6B?style=for-the-badge)](mailto:smithp17999@gmail.com?subject=Player%202%20has%20entered%20the%20game)
[![LinkedIn](https://img.shields.io/badge/💼_CO--OP-LinkedIn-0077B5?style=for-the-badge)](https://www.linkedin.com/in/smit-patne/)
[![Portfolio](https://img.shields.io/badge/🌐_WORLD_MAP-Portfolio-4ECDC4?style=for-the-badge)](https://smitpatneportfolio.netlify.app/)

<sub>Currently seeking: <b>GenAI · Full-Stack · Applied ML</b> roles · Let's build something legendary.</sub>

</div>
