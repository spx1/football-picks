from flask import Flask

def register_routes(app : Flask):
    from app.picks import register_routes as Picks
    from app.health import register_routes as Health
    Picks(app)
    Health(app)