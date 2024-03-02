import logging

logger = logging.getLogger(__name__)

def device_id_checked(token):
    try:
        if isinstance(token, str):
            return [token]
        else:
            return token
    except Exception as e:
        logger.error(f"device_id_checked | Error: {str(e)}", exc_info=True)
        return []
