"""
Trade Masker package.

Exposes main classes for convenience.
"""
from .watcher import TradeMaskerFileWatcher
from .processors.dummy import DummyMasker

__all__ = ["TradeMaskerFileWatcher", "DummyMasker"]