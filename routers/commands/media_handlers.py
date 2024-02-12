from aiogram import Router, F, types

from magic_filter import RegexpMode

from config import user, access
from database import insert_into_users_table, fetchall_sql_query

router = Router(name=__name__)



@router.message(F.text.regexp(r"^\S+$", mode=RegexpMode.MATCH))
async def register_login_handle(message: types.Message):
    if user.login != "" and user.password != "":
        await message.answer(
            text="You have loged in yet!"
        )
        return
    user.user_id = message.from_user.id
    if access.register == True:
        if user.login == "":
            user.login = message.text
            print(message.text)
            await message.answer(
                text="Enter the password:",
            )
        else:
            print(access.register)
            user.password = message.text
            print(user.password, user.login, user.user_id)
            login = user.login
            password = user.password
            user.empty()
            try:
                insert_into_users_table(login, password, user.user_id)
                access.register = False
                await message.answer(
                    text="Success!"
                )
            except Exception:
                await message.answer(
                    "You have been registered yet!\n"
                    "You need to login in your account!"
                )
    elif access.login == True:
        sql_query = "SELECT * FROM users"
        results = fetchall_sql_query(sql_query)
        user_id_in_result = False
        for result in results:
            if user.user_id == result[1]:
                user_id_in_result = True

        if not user_id_in_result:
            await message.answer(
                text="Your device is not authorized.\n"
                     " Please, click /register first"
            )
        if user.login == "":
            user.login = message.text
            for result in results:
                if user.user_id == result[1]:
                    if user.login == result[2]:
                        await message.answer(
                            text="Enter the password:",
                        )
                    else:
                        user.login = ""
                        await message.answer(
                            text="Login is incorrect.",
                        )
        else:
            user.password = message.text
            for result in results:
                if user.user_id == result[1]:
                    if user.password == result[3]:
                        await message.answer(
                            text="You have successfully loged in.",
                        )
                        return
                    else:
                        user.password = ""
                        await message.answer(
                            text="Password is incorrect.",
                        )
