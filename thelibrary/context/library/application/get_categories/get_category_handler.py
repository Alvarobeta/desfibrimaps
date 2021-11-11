from thelibrary.context.library.domain.category import CategoryRepository


class GetCategoryHandler:
    def __init__(
        self, 
        category_repository: CategoryRepository
    ):
        self.category_repository = category_repository


    def __call__(self, category_id: int):        
        category = self.category_repository.find_one_by_id(category_id=category_id)
        return category
