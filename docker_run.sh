if docker ps -a | grep -q -i django_tiktok
then
	docker stop django_tiktok ; docker rm django_tiktok
fi

docker run --name django_tiktok -d -p 8000:8000 -t django_tiktok
