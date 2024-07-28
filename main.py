from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
load_dotenv()
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}! Welcome to my CV bot. Use /help to see available commands.')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
Available commands:
/skills - View my key skills
/experience - See my work experience
/education - Check my educational background
/projects - View my notable projects
/contact - Get my contact information
    """
    await update.message.reply_text(help_text)

async def skills(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    skills_text = """
My Key Skills:
- Front End Web Design
- Blender 3D modelling
- GameDev in Godot Game Engine
    """
    await update.message.reply_text(skills_text)

async def experience(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    experience_text = """
Work Experience:
1. Worked in a small Indie Godot Game-dev group.
2. Made an educational resource sharing site for our college.
    """
    await update.message.reply_text(experience_text)

async def education(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    education_text = """
Education:
- Doing BTech in Information Technology in KBTCOE, Nashik.
    """
    await update.message.reply_text(education_text)

async def projects(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    projects_text = """
Notable Projects:
1. Developed an educational notes sharing website with interactable 3D model of our college.
    link: https://github.com/CampusConnectPBL/CampusConnect2

2. Created a simple site for getting some basic mathematical info about a number.
    link: https://github.com/Kushal-Dev94/Number_Info_site

3. Building a topdown tank game in Godot engine (WIP)
    link: https://github.com/Kushal-Dev94/TopDownTankGame
    """
    await update.message.reply_text(projects_text)

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    contact_text = """
Contact Information:
Email: kushalkishor31@gmail.com
LinkedIn: www.linkedin.com/in/kushal-shankhapal-20054b217
GitHub: github.com/Kushal-Dev94
    """
    await update.message.reply_text(contact_text)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("skills", skills))
app.add_handler(CommandHandler("experience", experience))
app.add_handler(CommandHandler("education", education))
app.add_handler(CommandHandler("projects", projects))
app.add_handler(CommandHandler("contact", contact))

print('Bot is running...')
app.run_polling()
