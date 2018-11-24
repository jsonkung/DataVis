function display_cards() {
    // do asynch post req to modify cards
    $('#cards').html('<img src=  "{{ url_for('static', filename='loading.gif') }}">');
    $.post("/choose_dataset", {
        query: $('#input_query').val()
    }).done(function(response) {

        title = response['title'];
        descriptions = response['descriptions'];

        console.log(title);
        console.log(descriptions);

        var section = document.getElementById('cards');
        section.innerHTML = '';
        for(let i=0; i<title.length; i++){
            let card = document.createElement('div');
            card.classList.add('ui');
            card.classList.add('card');

            let content = document.createElement('div');
            content.classList.add('content');
            let header = document.createElement('a');
            header.classList.add('header');
            header.text = title[i];
            let description = document.createElement('div');
            description.classList.add('description');
            description.append(descriptions[i]);
            content.appendChild(header);
            content.appendChild(description);
            console.log(content);

            let extraContent = document.createElement('div');
            extraContent.classList.add('extra');
            extraContent.classList.add('content');
            extraContent.insertAdjacentHTML('beforeend','<a><i class="chart line icon"></i> Plot Dataset</a>')

            card.appendChild(content);
            card.appendChild(extraContent);

            section.appendChild(card);
        }

    }).fail(function() {
        $('#cards').text("complete garbage")
    });
}
