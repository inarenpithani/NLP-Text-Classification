from hate.exception import CustomException
import sys

from hate.configuration.gcloud_syncer import GCloudSync

obj = GCloudSync()
obj.sync_folder_from_gcloud( 'hate-speech-nlp-2025','dataset.zip','download/dataset.zip')