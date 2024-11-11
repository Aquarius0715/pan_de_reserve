const lists = document.querySelectorAll('.list');
// console.log(lists)
let new_element = false;
let nextelem;
lists.forEach((list) => {
    const elm = list.querySelectorAll('a');
    list.addEventListener('click', () => {
        try{
            nextelem = list.nextElementSibling.tagName;
        }catch{
            nextelem = false;
        }
        try {
            const removeelem = document.querySelector('p')
            removeelem.remove();
        } catch {

        }
        if (nextelem != 'P') {
            // console.log(nextelem);
            new_element = document.createElement('p');
            new_element.innerHTML = `<div class="details">
                <div class="detail">                
                    <p><a>時間 </a><a>`+ elm[0].textContent + `</a></p>
                    <p><a>氏名 </a><a>`+ elm[1].textContent + `</a></p>
                </div>
                <div class="detail">
                    <p><a>予約内容</a></p>
                    <p><a>`+ elm[2].textContent + `</a></p></div>`;
            // console.log("-------------");
            list.after(new_element);
        }
    });
});