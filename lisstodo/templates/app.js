document.addEventListener('click', (e) => {
    const isDropdownBtn = e.target.classlist.contains('dropdown')
    
    if(!isDropdownBtn && e.target.closest('.navbar__item') != null) return;

    let currentSubmenu

    if(isDropdownBtn) {
        const item = e.target.closest('.menu_nav')

        currentSubmenu = item.querySelector('.submenu')

        currentSubmenu.classlist.toggle('show')
    }
})