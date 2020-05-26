import cv2

from gaze_tracking import GazeTracking
from scipy.spatial import distance
gaze = GazeTracking()
frameRate = 20.0

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        self.video.set(3, 400)
        self.video.set(4, 560)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):

        img_counter = 0
        success, image = self.video.read()
        im = cv2.imread("newmask.png")

        # cv2.rectangle(image, (400, 300), (700, 500), (178, 190, 181), 5)

        frame = cv2.flip(image, 2)
        # print("Frame size :", frame.shape[1])

        # gaze.refresh(frame)
        #
        # frame, x, y = gaze.annotated_frame()
        # text = ""
        #
        # left_pupil = gaze.pupil_left_coords()
        #
        # right_pupil = gaze.pupil_right_coords()
        # # print(right_pupil, left_pupil)
        #
        # points_cnt = (x, y)
        #
        # cv2.putText(frame, " click any key  ", (175, 17), cv2.FONT_HERSHEY_DUPLEX, 0.7,
        #             (0, 0, 0), 2)
        # if left_pupil and right_pupil != None:
        #     a = left_pupil
        #     b = right_pupil
        #     c = points_cnt
        #
        #
        #     dst_left = distance.euclidean(a, c)
        #     mm = 0.26458333
        #     dist_left_mm = (dst_left * mm) + 8
        #
        #     # print(dist_left_mm)
        #     # print("left:::", dist_left_mm)
        #     dst_right = distance.euclidean(b, c)
        #
        #     dist_right_mm = (dst_right * mm) + 8
        #     total_pd = dist_right_mm + dist_left_mm
        #     # print("total::", total_pd)
        #     # print("right::", dist_right_mm)
        #
        #     cv2.putText(frame, "Left PD:  " + str(dist_left_mm) + 'mm', (85, 125), cv2.FONT_HERSHEY_DUPLEX, 0.9,
        #                 (0, 0, 255), 1)
        #     cv2.putText(frame, "Right PD: " + str(dist_right_mm) + 'mm', (85, 175), cv2.FONT_HERSHEY_DUPLEX, 0.9,
        #                 (0, 0, 255), 1)
        #     k = cv2.waitKey(1)
        gaze.refresh(frame)

        frame, x, y = gaze.annotated_frame()
        text = ""

        # cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

        left_pupil = gaze.pupil_left_coords()

        right_pupil = gaze.pupil_right_coords()
        print(right_pupil, left_pupil)

        points_cnt = (x, y)

        # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # detector = dlib.get_frontal_face_detector()
        # predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        # faces = detector(frame)
        # for face in faces:
        #     landmarks = predictor(frame, face)
        #     landmarks_points = []
        #     for n in range(27, 28):
        #         x = landmarks.part(n).x
        #         y = landmarks.part(n).y
        #         landmarks_points.append((x, y))
        #         for m in landmarks_points:
        #             print(m)

        # print(points_cnt)
        if left_pupil and right_pupil != None:
            a = left_pupil
            b = right_pupil
            c = points_cnt
            # dist = [(a - c) ** 2 for a, c in zip(a, c)]
            # dist = math.sqrt(sum(dist))
            # print("new method",dist)

            dst_left = distance.euclidean(a, c)
            mm = 0.26458333
            dist_left_mm = (dst_left * mm) + 20

            #############################################################
            # tot_pix_dist = distance.euclidean(a,b)
            # print("pd_total",tot_pix_dist)
            # const = 40*tot_pix_dist
            # print("const: ", const)

            # tot_pix_dist = distance.euclidean(a, b)
            # print("pd_total", tot_pix_dist)
            # const = 50 * tot_pix_dist
            # print("const: ", const)
            # dis_from_cam = 5805.3854 / tot_pix_dist
            # print("Distance_from_cam : ", dis_from_cam)

            ##############################################################

            # print(dist_left_mm)
            print("left:::", dist_left_mm)
            dst_right = distance.euclidean(b, c)
            # print(dst_right)
            # print(dst_left)

            dist_right_mm = (dst_right * mm) + 20
            total_pd = dist_right_mm + dist_left_mm
            print("total::", total_pd)
            print("right::", dist_right_mm)

            cv2.putText(frame, "Left PD:  " + str(dist_left_mm) + 'mm', (85, 125), cv2.FONT_HERSHEY_DUPLEX, 0.9,
                        (0, 0, 255), 1)
            cv2.putText(frame, "Right PD: " + str(dist_right_mm) + 'mm', (85, 175), cv2.FONT_HERSHEY_DUPLEX, 0.9,
                        (0, 0, 255), 1)
            cv2.putText(frame, "Total PD: " + str(total_pd) + 'mm', (85, 200), cv2.FONT_HERSHEY_DUPLEX, 0.9,
                        (0, 0, 255), 1)

        im = cv2.resize(im, frame.shape[1::-1], interpolation=cv2.INTER_AREA)
        dst = cv2.addWeighted(frame, 0.5, im, 0.5, 0)
        flip = cv2.flip(dst, 1)
        # for i in range(3):
        #         img_name = "opencv_frame_{}.png".format(img_counter)
        #         cv2.imwrite(img_name, frame)
        #         print("{} written!".format(img_name))
        #         img_counter += 1



        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.

        ret, jpeg = cv2.imencode('.jpg', dst)
        return jpeg.tobytes()






