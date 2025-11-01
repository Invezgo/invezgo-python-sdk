"""Modules for Invezgo SDK."""

from .analysis import AnalysisModule
from .watchlists import WatchlistsModule
from .journals import JournalsModule
from .portfolios import PortfoliosModule
from .ai import AIModule
from .posts import PostsModule
from .profile import ProfileModule
from .membership import MembershipModule
from .trades import TradesModule
from .screener import ScreenerModule
from .search import SearchModule
from .health import HealthModule

__all__ = [
    "AnalysisModule",
    "WatchlistsModule",
    "JournalsModule",
    "PortfoliosModule",
    "AIModule",
    "PostsModule",
    "ProfileModule",
    "MembershipModule",
    "TradesModule",
    "ScreenerModule",
    "SearchModule",
    "HealthModule",
]

