const searchInput =
document.getElementById(
    "movie-search"
);

const suggestionsBox =
document.getElementById(
    "suggestions"
);

if(searchInput){

searchInput.addEventListener(
"input",
async function(){

    const query =
    this.value;

    if(query.length < 2){

        suggestionsBox
        .innerHTML = "";

        return;
    }

    try{

        const response =
        await fetch(
        `/suggest?query=${query}`
        );

        const data =
        await response.json();

        suggestionsBox
        .innerHTML = "";

        data.movies.forEach(
        movie => {

            const div =
            document
            .createElement("div");

            div.classList.add(
            "suggestion-item"
            );

            div.innerText =
            movie;

            div.onclick =
            () => {

                searchInput
                .value = movie;

                suggestionsBox
                .innerHTML = "";
            };

            suggestionsBox
            .appendChild(div);
        });

    } catch(error){
        console.log(error);
    }
});
}