from django.core.management.base import BaseCommand
from token_setter.utils import connect_obs_client, get_metadata, refresh


class Command(BaseCommand):
    def handle(self, *args, **options):
        obs_client = connect_obs_client()
        _, refresh_token = get_metadata(obs_client)
        refresh(obs_client, refresh_token)
