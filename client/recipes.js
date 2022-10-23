class Recipes {
    constructor() {}
    searchRecipes(ingredient, dairyFree, glutenFree) {
        return $.get(
            `/recipes/${ingredient}?dairy_free=${dairyFree}&gluten_free=${glutenFree}`
        );
    }
}
