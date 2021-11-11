from thelibrary.context.library.domain.category import CategoryRepository


class GetCategoriesHandler:
    def __init__(
        self, 
        category_repository: CategoryRepository
    ):
        self.category_repository = category_repository


    def __call__(self):        
        categories = self.category_repository.find_categories()
        return categories
