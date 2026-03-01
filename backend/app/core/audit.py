import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("smarthire_audit")

def log_agent_decision(agent_name: str, decision: str, context: dict):
    timestamp = datetime.utcnow().isoformat()
    log_entry = f"[{timestamp}] AGENT: {agent_name} | DECISION: {decision} | CONTEXT: {context}"
    logger.info(log_entry)
    # In production, this would write to a DB or specialized audit log service
