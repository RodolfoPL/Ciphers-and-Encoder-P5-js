// A code for base 64 encode and decode

let btnFile;
let btnAction;
let txtInput;
let txtOutput;
let operationInput;
let btnSave;

let operation = "encode";

function setup() {
  createCanvas(windowWidth, windowHeight);

  operationInput = createSelect();
  operationInput.option("ENCODE");
  operationInput.option("DECODE");
  operationInput.position(20, 20);

  txtInput = createElement("textarea", "Write (or paste) here");
  txtInput.position(20, 50);
  txtInput.size(width - 60, (height - 200) / 2);

  btnAction = createButton("Encode");
  btnAction.mousePressed(base64);
  btnAction.position(20, (height - 200) / 2 + 65);

  btnFile = createFileInput(handleFile);
  btnFile.position(105, (height - 200) / 2 + 65);
  btnFile.size(width - 60, (height - 200) / 2);

  txtOutput = createElement("textarea", "Result goes here");
  txtOutput.position(20, (height - 120) / 2 + 50);
  txtOutput.size(width - 60, (height - 200) / 2);

  btnSave = createButton("Download result into a .txt file");
  btnSave.mousePressed(saveFile);
  btnSave.position(20, height - 90);
}

function draw() {
  background(140, 144, 255);
  selectOperation();
}

function selectOperation() {
  switch (operationInput.value()) {
    case "ENCODE": {
      operation = "encode";
      btnAction.html("ENCODE");
      text(
        "Write a message on the input to encode in base 64 or load a file",
        110,
        35
      );
      textSize(15);
      break;
    }
    case "DECODE": {
      operation = "decode";
      btnAction.html("DECODE");
      text("Decode from Base64 format", 110, 35);
      break;
    }
  }
}

function base64() {
  let msg = txtInput.value();
  let result = "";
  print(msg);
  switch (operation) {
    case "encode": {
      result = btoa(unescape(encodeURIComponent(msg)));
      break;
    }
    case "decode": {
      result = decodeURIComponent(escape(atob(msg)));
    }
  }
  //
  // print(result);
  txtOutput.value(result);
}

function handleFile(file) {
  print(file);

  txtInput.value(file.data);
  base64();
}

function getDate() {
  let currentDate = new Date();

  let y = year();
  let M = month();
  let d = day();

  let h = hour();
  let m = minute();
  let s = second();

  let date = y + "" + M + "" + d + "" + h + "" + m + "" + s;
  print(date);
  return date;
}

function saveFile() {
  let filename = operation + '' + getDate() + '';
  let result = txtOutput.value();
  save(result, filename);
}
