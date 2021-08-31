//once content loaded attache event listeners to buttons
document.addEventListener('DOMContentLoaded', function() {
   console.log("DOM loaded")
   //hide compose view
   document.querySelector('#createNewPost-view').style.display = 'none';
    //add event listeners to buttons
    document.querySelector('#createNewPost').addEventListener('click', () => compose('compose'));
    document.querySelector('#cancelNewPost').addEventListener('click', ()=>{
        document.querySelector('#createNewPost-view').style.display = 'none';
    })
});

function compose(type){
    console.log("loading compose form");
    document.querySelector('#createNewPost-view').style.display = 'block';
}