-- SQLite
INSERT INTO content_feed (id, user_id, nickname, profile_image, content, image, is_marked, like_count)
VALUES 
(1, '111', 'smkim1', "http://img.marieclairekorea.com/2017/01/mck_586f4006b4e9f-375x375.jpg", "첫글입니다", "https://mblogthumb-phinf.pstatic.net/20150109_32/dpaaksndpf1_1420737682470GfGRp_JPEG/galaxy_4-wallpaper-1920x1080.jpg?type=w2", True, 10),
(2, '222', 'yu_99', "https://images.chosun.com/resizer/XdUHAMF4ZGd_4l8Ze0lyx93Z37Y=/464x0/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/6UHBHL2DZ7ISPMQ5UO6XAHUYNQ.jpg", True, 50),
(3, '333', 'aks92', "http://img.marieclairekorea.com/2017/01/mck_586f4006b4e9f-375x375.jpg", "세번째글입니다", "https://png.pngtree.com/background/20210716/original/pngtree-tranquil-universe-background-picture-image_1337175.jpg", True, 77);

INSERT INTO content_reply (id, nickname, content)
VALUES
(1, 'SMKI_M', '하잉하잉 사진이 이쁘네요'), 
(2, 'SOYEON_94', '히히힣'), 
(3, 'YSUJD_00', '키키킿'), 
(4, 'KKK_99', '끌끌끌');

INSERT INTO user_user (id, user_id, name, nickname, profile_image)
VALUES
(1, '111', 'smkim1', '김선민', "http://img.marieclairekorea.com/2017/01/mck_586f4006b4e9f-375x375.jpg");
