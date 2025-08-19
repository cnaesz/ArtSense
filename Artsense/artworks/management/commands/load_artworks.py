# artworks/management/commands/load_artworks.py
from django.core.management.base import BaseCommand
from artworks.models import Artwork
import requests
import time

class Command(BaseCommand):
    help = 'Fetch specific artworks from The Met API by Object Numbers (even if exact match fails)'

    def handle(self, *args, **options):
        # ✏️ Your list of object numbers
        object_numbers = [
            "67.187.211",
            "19.70",
            "29.100.68",
            "17.190.482",
            "88.3.20",
            # Add more...
        ]

        saved_count = 0

        for obj_num in object_numbers:
            time.sleep(0.2)  # Be kind to the API
            self.stdout.write(f"🔍 Searching for: {obj_num}")

            try:
                # Step 1: Use search API to find object by accession number
                search_url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={obj_num}&hasImages=true"
                search_res = requests.get(search_url)
                if search_res.status_code != 200:
                    self.stdout.write(self.style.WARNING(f"❌ API error for {obj_num}"))
                    continue

                search_data = search_res.json()
                object_ids = search_data.get('objectIDs')

                if not object_ids or len(object_ids) == 0:
                    self.stdout.write(self.style.WARNING(f"❌ No results found for {obj_num}"))
                    continue

                # Take the first match (usually the best one)
                object_id = object_ids[0]
                self.stdout.write(f"✅ Found Object ID: {object_id}")

                # Step 2: Get full details
                detail_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object_id}"
                detail_res = requests.get(detail_url)
                if detail_res.status_code != 200:
                    self.stdout.write(self.style.WARNING(f"❌ Failed to fetch details for ID {object_id}"))
                    continue

                artwork = detail_res.json()

                # Extract data
                title = artwork.get('title') or 'Untitled'
                artist = artwork.get('artistDisplayName') or 'Unknown Artist'
                image_url = artwork.get('primaryImage', '')
                accession_number = artwork.get('accessionNumber', obj_num)

                if not image_url:
                    self.stdout.write(self.style.WARNING(f"🖼️ No image: {title}"))
                    continue

                # Step 3: Save to database
                Artwork.objects.update_or_create(
                    met_id=object_id,
                    defaults={
                        'object_number': accession_number,
                        'title': title,
                        'artist': artist,
                        'image_url': image_url,
                    }
                )
                self.stdout.write(self.style.SUCCESS(f"💾 Saved: {title} by {artist}"))
                saved_count += 1

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"💥 Error processing {obj_num}: {e}"))

        self.stdout.write(
            self.style.SUCCESS(f"🎉 Done! Successfully saved {saved_count} artworks.")
        )