progetto di corso Emanuele Bruno

il progetto è stato sviluppato usando jupyter notebook e i file che contengono il codice sorgente sono dei notebook da aprire in jupyter

il progetto cerca i file del dataset nella cartella del progetto stesso, il file csv diagnoses_icd deve essere nella cartella hosp, i file csv admissions e patients devono essere nella cartella stessa del progetto
(ho messo uno screenshot della struttura della cartella nella repository "structure.pdf"), per quanto riguarda i csv df1, diag e admpat verranno creati dal codice del progetto che va eseguito nel seguente ordine:

- come prima cosa estrarre i file rar contenenti le porzioni di dataset usati

- i notebook admpat.ipynb e diag.ipynb sono i primi da aprire e contengono un'esplorazione iniziale 
delle tabelle patients, admissions e diagnosis_icd. questi primi notebook contengono anche la riorganizzazione delle tabelle
al fine di unirle e poter effettuare poi un'ananlisi più completa e delle predizioni.
il notebook diag.ipynb contiene anche il riferimento a uno script (contenuto nella cartella converter_icd-9) che è stato reperito su github 
e leggemente modificato al fine di tradurre i codici delle diagnosi icd9 nella codifica icd10.

- il notebook ihm contiene l'esplorazione e l'analisi dei dati che precede l'inizio dell'addestramento dei modelli usati.
il file contine poi lo studio fatto sull'in hospital mortality e le predizioni usando alcuni modelli con e senza crossvalidation,
l'applicazione dell'oversampling per bilanciare il dataset, un'analisi utilizzando un set di validazione e, il tuning degli iperparametri e le predizioni finali

- successivamente i notebook ehr_riad30/90/365 contengono analoghi passaggi per la predizione della riammissione in ospedale entro un determinato numero di giorni