"""Pre-charge le modele LLM en RAM (a lancer avant une demo live).

Usage : python -m scripts.warmup
"""
from __future__ import annotations

from src.rag.llm_client import get_llm
from src.utils.logger import logger


def main() -> None:
    logger.info("Prechauffage du LLM...")
    get_llm().warmup()
    logger.info("LLM pret pour la demo.")


if __name__ == "__main__":
    main()
