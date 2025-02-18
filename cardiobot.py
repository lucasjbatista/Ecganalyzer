
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import logging

# Configuração de logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Função para iniciar o bot
async def start(update: Update, context: CallbackContext):
    logger.info("Usuário enviou o comando /start")
    await update.message.reply_text("Bem-vindo ao CardioBot! Envie a foto do ECG para análise.")

# Função para receber a foto do ECG
async def handle_photo(update: Update, context: CallbackContext):
    logger.info("Usuário enviou uma foto")
    await update.message.reply_text("Foto do ECG recebida. Agora, informe a idade e o sexo do paciente.")

# Função principal
def main():
    # Substitua pelo token que o BotFather forneceu
    token = "8125975031:AAHvHLuVKkMdrehLNHopUES-vut0j_3TTx8"
    
    # Cria a aplicação
    application = Application.builder().token(token).build()

    # Adiciona os comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    # Inicia o bot
    logger.info("Bot iniciado...")
    application.run_polling()

if __name__ == "__main__":
    main()
