# Bot Pubblicitario Telegram

Questo progetto è un bot Telegram progettato per inviare messaggi promozionali a gruppi specifici su Telegram. Il bot è stato implementato utilizzando la libreria `python-telegram-bot` per Python.

## Funzionalità

Il bot offre le seguenti funzionalità:

- Invio di messaggi promozionali a gruppi specifici su Telegram.
- Modifica del messaggio promozionale.
- Visualizzazione degli ID dei gruppi in cui vengono inviati i messaggi promozionali.
- Aggiunta manuale di ID di gruppi per l'invio dei messaggi promozionali.
- Impostazione del numero di messaggi promozionali da inviare al giorno per gruppo.
- Fermare temporaneamente l'invio dei messaggi promozionali.
- Ferma il bot.

## Come utilizzare il bot

Per utilizzare il bot, è necessario seguire i passaggi:

1. Avviare il bot utilizzando il comando `/start`.
2. Modificare il messaggio promozionale utilizzando il comando `/editmessage [nuovo messaggio]`.
3. Aggiungere manualmente gli ID dei gruppi utilizzando il comando `/aggiungiidgruppo`.
4. Impostare il numero di messaggi promozionali da inviare al giorno per gruppo utilizzando il comando `/setNmessaggi [numero]`.
5. Inviare il messaggio promozionale a tutti i gruppi utilizzando il comando `/invio`.
6. Fermare temporaneamente l'invio dei messaggi promozionali utilizzando il comando `/stop`.
7. Consultare l'elenco dei comandi disponibili utilizzando il comando `/help`.
   P.S.(il bot deve essere nei gruppi coi permessi)

## Requisiti

Per eseguire il bot è necessario disporre di Python e delle seguenti librerie:

- `python-telegram-bot`: Per l'interfacciamento con l'API di Telegram.
- `random`: Per la generazione di numeri casuali.
- `time`: Per la gestione del tempo.

