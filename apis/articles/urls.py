from rest_framework import routers
from .api import ArticleViewset, RecentArticles, PersonalArticles

router = routers.DefaultRouter()

router.register('api/articles', ArticleViewset, 'articles')
router.register('api/recent', RecentArticles, 'recent')
router.register('api/personal', PersonalArticles, 'personal')

urlpatterns = router.urls