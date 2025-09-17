import firebase_admin
from firebase_admin import credentials, firestore

class FirestoreDB:
    """
    A client for interacting with Firestore.
    This class follows the Singleton pattern to ensure only one instance is created.
    """
    _instance = None

    @staticmethod
    def initialize():
        """Initializes the Firestore client."""
        if not FirestoreDB._instance:
            cred = credentials.ApplicationDefault()
            firebase_admin.initialize_app(cred)
            FirestoreDB._instance = firestore.client()

    @staticmethod
    def get_instance():
        """Returns the Firestore client instance."""
        if not FirestoreDB._instance:
            raise Exception("Firestore has not been initialized. Call FirestoreDB.initialize() first.")
        return FirestoreDB._instance

    def get_document(self, collection: str, document_id: str):
        """
        Retrieves a document from a Firestore collection.

        Args:
            collection (str): The name of the collection.
            document_id (str): The ID of the document.

        Returns:
            dict: The document data, or None if it doesn't exist.
        """
        doc_ref = self.get_instance().collection(collection).document(document_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        return None

    def set_document(self, collection: str, document_id: str, data: dict):
        """
        Creates or overwrites a document in a Firestore collection.

        Args:
            collection (str): The name of the collection.
            document_id (str): The ID of the document.
            data (dict): The data to store in the document.
        """
        self.get_instance().collection(collection).document(document_id).set(data)