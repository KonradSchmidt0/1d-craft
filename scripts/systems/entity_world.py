from scripts.Olympus import Olympus
from scripts.entities.interfaces.IEntityUpdatable import IEntityUpdatable


def process_entities(olympus: Olympus, dt):
    requests = []

    for e in olympus.entities:
        if not isinstance(e, IEntityUpdatable):
            continue

        new_requests = e.update(olympus, dt)

        if new_requests is None:
            continue

        for req in new_requests:
            requests.append(req)

    return requests

