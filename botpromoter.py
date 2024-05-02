import random
import time
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Lista degli ID dei gruppi in cui inviare i messaggi spam
gruppi_spam = [-1002037545391]

# Messaggio promozionale
messaggio_promozionale = "🎉🛍 Scopri le offerte imperdibili! Entra nel nostro gruppo Telegram @OFFERTE_ED_ERRORI_AMAZON e rimani sempre aggiornato sugli sconti incredibili su prodotti di qualità! 🎁✨ Siamo qui per offrirti un'esperienza di shopping eccezionale, dove troverai prezzi convenienti e offerte vantaggiose! 💰🚀 Unisciti a noi ora e inizia a risparmiare mentre ti diverti a fare shopping! 🤑🛒 #Offerte #ShoppingIntelligente #Risparmio"

# Numero predefinito di messaggi al giorno per gruppo
num_messaggi_giornalieri = 3

# Variabile per controllare se l'invio dei messaggi è attivo
invio_attivo = True

# Funzione per inviare il messaggio promozionale nei gruppi
def invia_messaggio_promozionale(context: CallbackContext) -> None:
    global invio_attivo
    if not invio_attivo:
        return  # Non fare nulla se l'invio non è attivo
    for gruppo_id in gruppi_spam:
        for _ in range(num_messaggi_giornalieri):
            context.bot.send_message(gruppo_id, messaggio_promozionale)
            # Attendi un po' prima di inviare il prossimo messaggio (opzionale)
            time.sleep(random.randint(1, 10))

# Funzione per gestire il comando /stop
def stop(update: Update, context: CallbackContext) -> None:
    global invio_attivo
    invio_attivo = False
    update.message.reply_text("Invio dei messaggi promozionali interrotto.")


# Funzione per gestire il comando /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Benvenuto! Sono attivo e funzionante.")
    # Avvia l'invio del messaggio promozionale nei gruppi
    context.job_queue.run_repeating(invia_messaggio_promozionale, interval=86400, first=random.randint(1, 86400))

# Funzione per gestire il comando /editmessage
def edit_message(update: Update, context: CallbackContext) -> None:
    global messaggio_promozionale
    if len(context.args) == 0:
        # Invia il messaggio promozionale attuale
        update.message.reply_text(f"Messaggio promozionale attuale:\n{messaggio_promozionale}")
    else:
        # Ottiene il nuovo messaggio dall'input dell'utente
        nuovo_messaggio = " ".join(context.args)
        messaggio_promozionale = nuovo_messaggio
        update.message.reply_text("Messaggio promozionale modificato con successo.")

# Funzione per gestire il comando /gruppi
def gruppi_info(update: Update, context: CallbackContext) -> None:
    if len(gruppi_spam) > 0:
        # Costruisci il testo con l'elenco degli ID dei gruppi
        text = f"Elenco dei gruppi in cui inviare i messaggi spam:\n"
        for gruppo_id in gruppi_spam:
            text += f"{gruppo_id}\n"
        update.message.reply_text(text)
    else:
        update.message.reply_text("Nessun gruppo aggiunto per l'invio dei messaggi spam.")

# Funzione per gestire il comando /aggiungiidgruppo
def aggiungi_id_gruppo(update: Update, context: CallbackContext) -> None:
    global gruppi_spam
    # Ottiene l'ID del gruppo dall'input dell'utente
    try:
        gruppo_id = int(context.args[0])
        # Aggiunge l'ID del gruppo alla lista
        if gruppo_id not in gruppi_spam:
            gruppi_spam.append(gruppo_id)
            update.message.reply_text("ID del gruppo aggiunto con successo per l'invio dei messaggi spam.")
        else:
            update.message.reply_text("Questo ID del gruppo è già stato aggiunto per l'invio dei messaggi spam.")
    except (IndexError, ValueError):
        update.message.reply_text("Inserisci un ID di gruppo valido.")

# Funzione per gestire il comando /setNmessaggi
def set_num_messaggi(update: Update, context: CallbackContext) -> None:
    global num_messaggi_giornalieri
    # Ottiene il numero di messaggi dal parametro
    try:
        num_messaggi = int(context.args[0])
        update.message.reply_text(f"Numero di messaggi giornalieri impostato a {num_messaggi}. (Attuale: {num_messaggi_giornalieri})")
        num_messaggi_giornalieri = num_messaggi
    except (IndexError, ValueError):
        update.message.reply_text("Utilizzo corretto: /setNmessaggi <numero>")

# Funzione per gestire il comando /invio
def invio(update: Update, context: CallbackContext) -> None:
    # Verifica se ci sono gruppi nella lista
    if len(gruppi_spam) > 0:
        # Invia il messaggio promozionale a tutti i gruppi nella lista
        for gruppo_id in gruppi_spam:
            context.bot.send_message(gruppo_id, messaggio_promozionale)
        update.message.reply_text("Messaggio inviato a tutti i gruppi.")
    else:
        update.message.reply_text("Nessun gruppo presente nella lista.")


# Funzione per gestire il comando /stop
def stop(update: Update, context: CallbackContext) -> None:
    global invio_attivo
    invio_attivo = False
    update.message.reply_text("Invio dei messaggi promozionali interrotto.")

# Funzione per gestire il comando /help
def help_command(update: Update, context: CallbackContext) -> None:
    help_text = (
        "Ecco i comandi disponibili:\n\n"
        "/start - Avvia il bot\n"
        "/editmessage [nuovo messaggio] - Modifica il messaggio promozionale\n"
        "/gruppi - Visualizza l'elenco degli ID dei gruppi in cui inviare i messaggi spam\n"
        "/aggiungiidgruppo - Aggiunge manualmente un ID di gruppo per l'invio dei messaggi spam\n"
        "/setNmessaggi [numero] - Imposta il numero di messaggi promozionali da inviare al giorno per gruppo\n"
        "/invio - Invia il messaggio promozionale a tutti i gruppi\n"
        "/stop - Ferma il bot\n"
        "/help - Mostra questo messaggio di aiuto"
    )
    update.message.reply_text(help_text)

def main() -> None:
    # Inizializza il bot con il token
    global updater
    updater = Updater("your_token_________")

    # Ottieni il dispatcher per registrare i comandi
    dispatcher = updater.dispatcher

    # Registra i gestori per i comandi
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("editmessage", edit_message))
    dispatcher.add_handler(CommandHandler("gruppi", gruppi_info))
    dispatcher.add_handler(CommandHandler("aggiungiidgruppo", aggiungi_id_gruppo))
    dispatcher.add_handler(CommandHandler("setNmessaggi", set_num_messaggi))
    dispatcher.add_handler(CommandHandler("invio", invio))
    dispatcher.add_handler(CommandHandler("stop", stop))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Avvia il bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
