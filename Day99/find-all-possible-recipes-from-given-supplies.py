class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        df = {}
        able = defaultdict(bool)

        for sup in supplies:
            able[sup] = True

        for i in range(len(recipes)):
            df[recipes[i]] = ingredients[i]

        def dfs(recipe,visited):
            if able[recipe] or recipe in visited:
                return able[recipe]

            visited.add(recipe)

            if recipe not in df:
                return False

            produced = True
            for u in df[recipe]:
                if not dfs(u,visited):
                    produced = False
                    break
            able[recipe] = produced
            return produced
            
        result = []
        for recipe in recipes:
            if able[recipe] or dfs(recipe,set()):
                result.append(recipe)
        return result

