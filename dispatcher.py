from aiogram import Dispatcher


def get_dp():
    from handlers.start import start_router
    dp = Dispatcher()
    dp.include_routers(
        start_router
    )
    return dp