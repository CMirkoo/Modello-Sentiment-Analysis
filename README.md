# Modello di Sentiment Analysis con CI/CD e Monitoring

Questo progetto espone un'API REST per l'analisi del sentiment di un testo. L'infrastruttura è completamente containerizzata con Docker e include una pipeline CI/CD gestita da Jenkins per l'automazione di build, test e deploy, oltre a un sistema di monitoraggio completo con Prometheus e Grafana.

---

## Funzionalità

* **API di Sentiment Analysis**: Un endpoint `/predict` che riceve del testo e restituisce un'analisi del sentiment.
* **Pipeline CI/CD Automatizzata**: Un `Jenkinsfile` che orchestra l'intero ciclo di vita del software:
    * Checkout del codice da Git.
    * Build delle immagini Docker.
    * Esecuzione di test automatici con `pytest`.
    * Deploy dell'intera applicazione.
* **Monitoraggio Completo**:
    * **Prometheus** per la raccolta di metriche applicative e di sistema.
    * **cAdvisor** per il monitoraggio dettagliato delle risorse dei container (CPU, Memoria).
    * **Grafana** per la visualizzazione dei dati attraverso dashboard interattive.

---

## Stack Tecnologico

* **Backend**: Python, FastAPI
* **Machine Learning**: Scikit-learn
* **Containerizzazione**: Docker, Docker Compose
* **CI/CD**: Jenkins
* **Monitoring**: Prometheus, Grafana, cAdvisor
* **Web Server/Proxy**: Nginx

---

## Come Avviare il Progetto in Locale

Per eseguire l'intero stack sul tuo computer, segui questi passaggi.

### Prerequisiti

Assicurati di avere installato:
* [Git](https://git-scm.com/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Installazione e Avvio

1.  **Clona il repository (se invitato) o scompatta il file ZIP:**
    ```bash
    git clone [https://github.com/NotMirko/Modello-Sentiment-Analysis.git](https://github.com/NotMirko/Modello-Sentiment-Analysis.git)
    ```

2.  **Entra nella cartella del progetto:**
    ```bash
    cd Modello-Sentiment-Analysis
    ```

3.  **Avvia tutti i servizi con Docker Compose:**
    Questo comando costruirà le immagini e avvierà tutti i container (App, Nginx, Prometheus, cAdvisor, Grafana).
    ```bash
    docker compose -f configuration/docker-compose.yml up --build
    ```

---

## Accesso ai Servizi

Una volta che i container sono in esecuzione, puoi accedere ai vari servizi:

* **API di Sentiment Analysis**: `http://localhost`
    * Usa Postman o un altro client per inviare richieste `POST` all'endpoint `/predict`.
* **Prometheus**: `http://localhost:9090`
    * Puoi esplorare le metriche raccolte e verificare lo stato dei target.
* **Grafana**: `http://localhost:3000`
    * **Utente:** `admin`
    * **Password:** `admin` (ti verrà chiesto di cambiarla al primo accesso).
* **cAdvisor**: `http://localhost:7070`
    * Interfaccia per il monitoraggio in tempo reale dei container.

---

##  Impostazione della Pipeline Jenkins (Opzionale)

Se vuoi replicare l'ambiente di automazione:
1.  Avvia un'istanza di Jenkins (preferibilmente con Docker).
2.  Crea un nuovo job di tipo **"Pipeline"**.
3.  Nella configurazione del job, imposta "Definition" su **"Pipeline script from SCM"**.
4.  Imposta "SCM" su **"Git"** e inserisci l'URL di questo repository.
5.  Crea le credenziali per GitHub in Jenkins e aggiorna la variabile `GIT_CREDS` nel `Jenkinsfile`.
6.  Salva e avvia la build.