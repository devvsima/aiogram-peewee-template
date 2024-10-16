from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import dp, bot, _

import speech_recognition as sr
from pydub import AudioSegment
import os


from data.config import DIR
# Функция для конвертации ogg в wav
def convert_ogg_to_wav(ogg_path):
    audio = AudioSegment.from_ogg(ogg_path)
    wav_path = ogg_path.replace(".ogg", ".wav")
    audio.export(wav_path, format="wav")
    return wav_path

# Обработчик голосового сообщения
@dp.message_handler(content_types=types.ContentType.VOICE)
async def handle_voice(message: types.Message):
    # Скачиваем голосовое сообщение
    voice = await message.voice.download()

    # Конвертируем ogg в wav
    path = f"{DIR}/{voice.name}"
    print(path)
    wav_path = convert_ogg_to_wav(path)

    
    # Распознаем голос с помощью SpeechRecognition
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="ru-RU")  # Выбор языка
            
            await message.reply(f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a> Изложил ебически важную инфу: <blockquote>{text}</blockquote>")
        except sr.UnknownValueError:
            await message.reply("Нихуй не ясно, но ебать как интересно.")
        except sr.RequestError as e:
            print(f"Ошибка запроса к Google Speech API: {e}")
    
    # Удаляем файлы после обработки
    os.remove(f"{DIR}/{voice.name}")
    os.remove(f"{DIR}/{wav_path}")