            //extract the first matching element from the page with query selector
            function hello(){
                // use 'let' not 'const' if the variable will change. 
                const heading = document.querySelector('h1')
                //'===' strict equality '==' as long as types same
                if (heading.innerHTML === 'Hello'){
                    heading.innerHTML= "goodbye";
                }
                else{
                    document.querySelector('h1').innerHTML= "Hello";
                }
            }