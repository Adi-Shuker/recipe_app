const renderer = new Renderer();
const recipes = new Recipes();

$(".btn-search-recipes").on("click", () => {
    ingredient = $("#ingredient").val();
    dairyFree = $(".dairy-free")[0].checked;
    glutenFree = $(".gluten-free")[0].checked;
    recipes.searchRecipes(ingredient, dairyFree, glutenFree).then((recipes) => {
        renderer.render(recipes);
    });
});
