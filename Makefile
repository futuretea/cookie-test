all:
docker:
	docker build -t futuretea/cookie-test .
run:
	docker run -itd -p 80:80 --name cookie-test futuretea/cookie-test
