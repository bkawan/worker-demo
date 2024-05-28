from django.utils.timezone import now

from apps.v1.worker.models import Unit, Visit


def create_visit(*, unit_id: int, latitude: float, longitude: float) -> Visit:
    instance = Visit(
        unit_id=unit_id,
        latitude=latitude,
        longitude=longitude,
        datetime=now()
    )
    instance.full_clean()
    instance.save()
    return instance
