// SPDX-FileCopyRightText: Copyright (c) 2023-present Jeffrey LeBlanc
// SPDX-License-Indentifier: MIT

import "./css/index.css"

import {createApp} from "vue"
import {G} from "./global.js"
import DataManager from "./DataManager.js"
import MainApp from "./MainApp.vue"


function main(){

    // Make a data manager
    G.mng = new DataManager();

    // Create the main app
    G.app = createApp(MainApp);
    G.app.use(G);

    // Mount and export
    G.app.mount('#mount');

    // Kick off
    G.mng.fetch_posts();

    // Export to window for debugging
    if(window.$G===undefined){
        window.$G = G;
    }else{
        console.warn("window.$G already assigned.")
    }
}

main();

