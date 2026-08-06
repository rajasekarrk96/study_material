"""
Learning OS — Media Library Service.
Manages media uploads, folder organizational structures, tag associations, and targets references.
"""
import logging
from typing import List, Optional
from app.core.extensions import db
from app.domains.knowledge.models import Media, MediaFolder, MediaTag, MediaReference
from app.domains.content.models import Tag

logger = logging.getLogger("learning_os.media")


class MediaService:
    @staticmethod
    def get_or_create_folder(name: str) -> MediaFolder:
        """Get or create a MediaFolder by name."""
        folder = MediaFolder.query.filter_by(name=name).first()
        if not folder:
            folder = MediaFolder(name=name)
            db.session.add(folder)
            db.session.commit()
        return folder

    @staticmethod
    def list_folders() -> List[MediaFolder]:
        """List all media folders."""
        return MediaFolder.query.order_by(MediaFolder.name.asc()).all()

    @staticmethod
    def add_media(
        filename: str,
        url: str,
        file_type: str,
        file_size: int,
        folder_id: Optional[int] = None,
        created_by_id: Optional[int] = None
    ) -> Media:
        """Register a new media file in the library."""
        media = Media(
            filename=filename,
            url=url,
            file_type=file_type,
            file_size=file_size,
            folder_id=folder_id,
            created_by_id=created_by_id
        )
        db.session.add(media)
        db.session.commit()
        return media

    @staticmethod
    def delete_media(media_id: int) -> bool:
        """Remove a media record from the library."""
        media = db.session.get(Media, media_id)
        if media:
            db.session.delete(media)
            db.session.commit()
            return True
        return False

    @staticmethod
    def tag_media(media_id: int, tag_names: List[str]) -> None:
        """Associate tags with a media item."""
        media = db.session.get(Media, media_id)
        if not media:
            return

        # Clear existing media tag associations
        MediaTag.query.filter_by(media_id=media_id).delete()

        for name in tag_names:
            name_clean = name.strip()
            if not name_clean:
                continue
            # Find or create Tag
            tag = Tag.query.filter_by(name=name_clean).first()
            if not tag:
                # Generate simple slug
                slug = name_clean.lower().replace(" ", "-")
                tag = Tag(name=name_clean, slug=slug)
                db.session.add(tag)
                db.session.flush()
            
            # Create link
            assoc = MediaTag(media_id=media.id, tag_id=tag.id)
            db.session.add(assoc)
        
        db.session.commit()

    @staticmethod
    def add_reference(media_id: int, target_type: str, target_id: int) -> MediaReference:
        """Create a reference link from a topic/lesson/section to a media item."""
        ref = MediaReference.query.filter_by(
            media_id=media_id,
            target_type=target_type,
            target_id=target_id
        ).first()

        if not ref:
            ref = MediaReference(media_id=media_id, target_type=target_type, target_id=target_id)
            db.session.add(ref)
            db.session.commit()
        return ref

    @staticmethod
    def remove_reference(reference_id: int) -> bool:
        """Remove a media reference link."""
        ref = db.session.get(MediaReference, reference_id)
        if ref:
            db.session.delete(ref)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_referenced_media(target_type: str, target_id: int) -> List[Media]:
        """Retrieve all media files referenced by a specific target entity."""
        references = MediaReference.query.filter_by(target_type=target_type, target_id=target_id).all()
        media_ids = [ref.media_id for ref in references]
        if not media_ids:
            return []
        return Media.query.filter(Media.id.in_(media_ids)).all()
