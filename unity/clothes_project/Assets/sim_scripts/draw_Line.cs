using System.Collections;
using System.Collections.Generic;
using UnityEngine;


// This is a component of MainCamera
// drag to create a line
[RequireComponent(typeof(Camera))]
public class draw_Line : MonoBehaviour {

    private new Camera camera;

    public Material lineMaterial;
    public float lineWidth;
    private float depth = 1;

    private GameObject tableModel;
    private Vector3? table_pos;
    //public Material cubeMaterial;

    private Vector3? lineStartPoint = null;


	// Use this for initialization
	void Start () {
        camera = GetComponent<Camera>();

        // get clothes mesh
        tableModel = GameObject.Find("Our Model");
        if (!tableModel)
        {
            Debug.Log("Clothes Mesh not exist");
            return;
        }

        // world space
        table_pos = tableModel.transform.position;

	}
	
	// Update is called once per frame
	void Update () {

        // right click
        if (Input.GetMouseButtonDown(1))
        {
            lineStartPoint = GetMouseCameraPoint();
        }

        if (Input.GetMouseButtonUp(1))
        {
            if (!lineStartPoint.HasValue)
                return;

            //var lineEndPoint_local = GetMouseCameraPoint();
            var lineEndPoint = GetMouseCameraPoint();

            var RotationAxis = new GameObject("RotationAxis");
            var lineRenderer = RotationAxis.AddComponent<LineRenderer>();
            lineRenderer.material = lineMaterial;


            var start = new Vector3(lineStartPoint.Value.x, table_pos.Value.y, lineStartPoint.Value.z);
            var end = new Vector3(lineEndPoint.x, table_pos.Value.y, lineEndPoint.z);


            lineRenderer.SetPositions(new Vector3[] { lineStartPoint.Value, lineEndPoint });

            //lineRenderer.SetPositions(new Vector3[] { start, end });
            lineRenderer.startWidth = lineWidth;
            lineRenderer.endWidth = lineWidth;


            // create a cube as rotating center
            var cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
            //cube.transform.position = (lineEndPoint - lineStartPoint.Value) / 2;
            var cubeRenderer =cube.AddComponent<MeshRenderer>();

            // Suppose line is centered
            cube.transform.position = Vector3.Lerp(lineStartPoint.Value, lineEndPoint, 0.5f);

            //cubeRenderer.material = cubeMaterial;
            //cubeRenderer.material.SetColor("_Color", Color.red);
            cube.transform.localScale = new Vector3(0.15f, 0.15f, 0.15f);
            
            // To reset everything
            lineStartPoint = null;
        }

	}


    private Vector3 GetMouseCameraPoint()
    {
        
        var ray = camera.ScreenPointToRay(Input.mousePosition);

        return ray.origin + ray.direction * depth;
    }
}
