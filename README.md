---
__Aim__

-  To implement, build and deploy a scoring service for a live game.
-  This service exposes two methods via RestAPI, one is to fill a goal for respective team and one to display the overall score.



---

__Tools used__


- Docker
- Python3
- fastAPI framework

---
__Files__

- Dockerfile
- main.py in app directory

---
__Procedure and usage__

- Clone the repository.

- Enter into this directory 

__cd python-assignment__

- Build the docker image using the following command



__docker build -t my-app-image .__

- Run the docker container from the image.

__docker run -it --rm -p 8000:80 my-app-image__

 -p flag is to map the port 80 (tcp) on the container to the localhost port 8000.
 
 After this open a new terminal tab to execute curl or http commands for the expected outcomes.

__Expected outcomes__

- The outcomes can be observed in any web browser or from terminal.
- In terminal either Curl or HTTPie command-line tools can be used. 

```
~/python-assignment$ http -b http://localhost:8000/score

{

"away": 0,

"home": 0

}
```

```
~/python-assignment$ http -b http://localhost:8000/goal?team=away

{

"away": 1,

"home": 0

}
```

```
~/python-assignment$ http -b http://localhost:8000/goal?team=home

{

"away": 1,

"home": 1

}
```

```
~/python-assignment$ http -b http://localhost:8000/goal?team=home

{

"away": 1,

"home": 2

}
```

```
~/python-assignment$ http -b http://localhost:8000/score

{

"away": 1,

"home": 2

}

```
___

---

