if docker ps -a | grep -q -i django_tiktok
then
        docker stop django_tiktok ; docker rm django_tiktok
fi

docker run --name django_tiktok -d -p 80:80 -t django_tiktok
