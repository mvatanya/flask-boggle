
$("#form").on("submit", getResponse)

async function getResponse(evt) {
    evt.preventDefault();
    //console.log($("#input-word").val())
    
    let data = {data:$("#input-word").val()}
    let response = await axios.post("/check", data);
    await response.data;
    $("#response").text("result: "+response.data.result);
    if (response.data.result === "ok") {
        checkScore($("#input-word").val());
    }
    
}

let scores = 0;
let wordArray = [];
function checkScore(word){
    if(!wordArray.includes(word)){
            wordArray.push(word)
            scores += word.length
    }
   
    return scores
}




