const app = {

    $:{
        menu : document.querySelector('.menu'),
        sidebarContainer : document.querySelector('.sidebar-container'),
        sidebar : document.querySelector('.sidebar'),
    },

    init() {
        app.registerEventListener();
    },

    registerEventListener() {

        app.$.menu.addEventListener('click', (e)=>{
            app.$.sidebarContainer.style.visibility = 'visible';

            setTimeout(() => {
                document.addEventListener('click', (evnt) => {

                    function isChildOfSidebar(e) {
                        let children = app.$.sidebar.querySelectorAll('*');
                        for (const child of children){
                            if (e.target === child){
                                return false;
                            }
                        }
                        return true;
                    }
                    if (evnt.target != app.$.menu && evnt.target != app.$.sidebar && isChildOfSidebar(evnt)){
                      app.$.sidebarContainer.style.visibility = 'hidden';
                    }
                })
            }, 500);

        })
        
    }
}

window.addEventListener('load', app.init);