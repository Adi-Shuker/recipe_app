class Renderer {
    constructor() {}
    render(recipes) {
        const source = $("#recipes-template").html();
        const template = Handlebars.compile(source);
        let newHTML = template({ recipes: recipes });
        $(".recipes").empty();
        $(".recipes").append(newHTML);
    }
}
