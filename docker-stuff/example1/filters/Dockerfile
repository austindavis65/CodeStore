FROM ubuntu:20.04
RUN apt update -y && apt install filters fortune -y
ENV PATH=$PATH:/usr/games
ENV DOCK_EXAM=halloween
ADD app.sh /
ADD alice.txt /foo.txt

CMD ["/app.sh"]

