const icon = document.querySelector('#icon')
const menu = document.querySelector('#navicons');
const tag = document.querySelector('.tag')

// console.log(icon)
// console.log(menu)

icon.addEventListener('click', ()=>{
    if (menu.classList.contains('ladden')){
        menu.classList.remove('ladden');
    }
    else{
        menu.classList.add('ladden')
    }
})


icon.addEventListener('click', ()=>{
    if (tag.classList.contains('tag')){
        tag.classList.remove('tag');
    }
    else{
        tag.classList.add('tag')
    }
})