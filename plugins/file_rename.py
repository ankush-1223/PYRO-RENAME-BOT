@Client.on_message(filters.document | filters.audio | filters.video)
async def rename(client, message):
    file = message.document or message.video or message.audio
    if not file:
        return  # no supported file in the message

    file_id = file.file_id
    file_name = file.file_name
    file_unique_id = file.file_unique_id
    file_size = file.file_size

    # Store the file info in the database or dict
    media_info = {
        "file_name": file_name,
        "file_id": file_id,
        "file_unique_id": file_unique_id,
        "file_size": file_size
    }

    media_data[file_unique_id] = media_info

    # Ask user for new file name
    await message.reply_text(f"Current file name: `{file_name}`\n\nSend me the new file name (without extension).")
    user_steps[message.from_user.id] = file_unique_id
